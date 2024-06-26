import './SmallBox.css'

function SmallBox(props){
    const cls = props.num % 2 === 0? 'even' : (isPrime(props.num) ? 'prime' : 'odd');
    return(
        <>
        {
            !isPrime(props.num) && (
                <div id='sb-container' className={cls}>
                    <h1>{props.num}</h1>
                </div>
            )
        }
        {/* <div id='sb-container' className={cls}>
            <h1>{props.num}</h1>
        </div> */}
        </>
    )
}

function isPrime(num) {
    if (num <= 1) {
        return false;
    }
    for (let i = 2; i * i <= num; i++) {
        if (num % i === 0) {
            return false;
        }
    }
    return true;
}

export default SmallBox