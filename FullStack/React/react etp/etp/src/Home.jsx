import { Link } from "react-router-dom"

const Home = () => {
    return (
        <div>
            <h2>
                Below are the solutions for the today's question.
            </h2>
            <ul>
                <li>
                    <Link to="/q1">Question 1</Link>
                </li>
                <br />
                <li>
                    <Link to="/q2">Question 2</Link>
                </li>
                <br />
                <li>
                    <Link to="/q3">Question 3</Link>
                </li>
                <br />
                <li>
                    <Link to="/q5">Question 5</Link>
                </li>
                <br />
                <li>
                    <Link to="/q6">Question 6</Link>
                </li>
                <br />
                <li>
                    <Link to="/q7">Question 7</Link>
                </li>
                <br />
                <li>
                    <Link to="/q8">Question 8</Link>
                </li>
                <br />
                <li>
                    <Link to="/q9">Question 9</Link>
                </li>
                <br />
                <li>
                    <Link to="/q10">Question 10</Link>
                </li>
                <br />
                <li>
                    <Link to="/q11">Question 11</Link>
                </li>
                <br />
                <li>
                    <Link to="/q12">Question 12</Link>
                </li>
                <br />
                <li>
                    <Link to="/q13">Question 13</Link>
                </li>
                <br />
                <li>
                    <Link to="/q14">Question 14</Link>
                </li>
                <br />
                <li>
                    <Link to="/q15">Question 15</Link>
                </li>
            </ul>
        </div>
    )
}

export default Home