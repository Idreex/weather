import StudentList from './Students';
import { useState } from 'react';

function TeacherList(){

    const [changeText, setChangeText] = useState(false);

    function handleChangeText(){
        setChangeText(!changeText)
    }

    return(
        <div>
            <p>Student No</p>
            <button onClick={handleChangeText}>Click to Toggle</button>
            <StudentList changeText={changeText}/>
            
        </div>
    )
}



export default TeacherList