import { people } from "./data";
import utils from "./utils";

const List = () => {
    const Listitem = people.map(person =>
        <li key={person.id}>
            <img src={utils(person)}
            alt = {person.name}
            />
            <p>
                <b>{person.name}:</b>
                <em>{' '+person.profession+' '}</em>
                known for {person.achievement}

            </p>
        </li>
    )
  return (
    <>
        <ul>
        {Listitem}
        </ul>
    </>
  )
}


export default List