const http = require("http");
const url = require("url");
const PORT = 4000;

var data = [
];

function generateUniqueId() {
  const characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";
  let uniqueId = "";
  for (let i = 0; i < 6; i++) {
    uniqueId += characters.charAt(
      Math.floor(Math.random() * characters.length)
    );
  }
  return uniqueId;
}

const server = http.createServer((req, res) => {
  const parseURL = url.parse(req.url, true);
  const { pathname, query } = parseURL;
  const method = req.method;

  if (pathname === "/todos" && method === "GET") {
    res.writeHead(200, { "Content-Type": "application/Json" });
    res.end(JSON.stringify(data));
  } else if (pathname === "/todos/new" && method === "POST") {
    let body = "";

    req.on("data", (chunk) => {
      body += chunk.toString();
    });

    req.on("end", () => {
      try {
        const payload = JSON.parse(body);

        const { title, priority } = payload;

        if (!title || !priority) {
          res.writeHead(400, { "Content-Type": "application/Json" });
          res.end(JSON.stringify({ error: "Title and priority are required" }));
          return;
        }

        const newTask = {
          title: title,
          priority: priority,
          id: generateUniqueId(),
          status: "pending",
        };

        data.push(newTask);
        res.writeHead(201, { "Content-Type": "application/Json" });
        res.end(
          JSON.stringify({
            success: true,
            id: newTask.id,
          })
        );
      } catch (error) {
        res.writeHead(400, { "Content-Type": "application/Json" });
        res.end(JSON.stringify({ error: "Invalid request body" }));
      }
    });
  } else if (pathname === "/todos/delete" && method === "DELETE") {
    const { id } = query;

    const taskIndex = data.findIndex((task) => task.id === id);

    data.splice(taskIndex, 1);

    res.writeHead(200, { "Content-Type": "application/Json" });
    res.end(
      JSON.stringify({
        success: true,
      })
    );
  } else if (pathname === "/todos/update" && method === "PUT") {
    let body = "";

    req.on("data", (chunk) => {
      body += chunk.toString();
    });

    req.on("end", () => {
        const payload = JSON.parse(body);

        const { id,title, priority,status } = payload;

        const taskIndex = data.findIndex(task=>task.id===id)

        const oldTask = data[taskIndex]

        const newTask = {
            ...oldTask,
        }
        if(title){
            newTask.title = title
        }
        if(priority){
            newTask.priority = priority
        }
        if(status){
            newTask.status = status
        }

        data.splice(taskIndex, 1, newTask)

        res.writeHead(200, {"Content-Type" : "application/json"})
        res.end(JSON.stringify({
        success : true
      })
    );
    }
    )

  } else {
    res.writeHead(404, { "Content-Type": "application/Json" });
    res.end(JSON.stringify({ error: "Not found" }));
  }
});

server.listen(PORT, () => {
  console.log("Server running on port", PORT);
});
