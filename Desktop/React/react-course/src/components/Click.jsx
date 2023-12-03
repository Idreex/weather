import { useState } from "react";

const init = 0;

function Buttonclick() {
  const [counter, setCounter] = useState(init);

  function handleClickPlus() {
    setCounter(counter + 1);
    console.log(counter)
  }

  return (
    <div>
      <p>Counter {counter}</p>
      <button onClick={handleClickPlus}>Click +</button>
    </div>
  );
}

export default Buttonclick;
