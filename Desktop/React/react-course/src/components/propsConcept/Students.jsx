



function StudentList(props) {

  const {changeText} = props

  return (
    <div>
        <h4>StudentList</h4>
        {changeText ? (
          <p>The number in this class is 15</p>
          ) : null}
    </div>
  )
}

export default StudentList