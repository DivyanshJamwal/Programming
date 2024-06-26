function a(){
    var count = 1
    function b(){
        var count = 6
        console.log(count)
    }
    return b
}

const x = a()

x()