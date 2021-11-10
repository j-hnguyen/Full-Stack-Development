async function makeTable(data, table)
{
    data = data.split(",");
    var table = document.getElementById(table);
    while (table.rows.length > 0) // clear table
    {
        table.deleteRow(0);
    }
    for (var i = 0; i < data.length; i++) 
    {
        var nameGrade = data[i].replace(/\"/g, "").replace(/{/g, "").replace(/}/g, "").split(":"); // easy way to remove " { }
        var row = 
                `<tr>
                    <td>${nameGrade[0]}</td>
                    <td>${nameGrade[1]}</td>
                </tr>`
        table.innerHTML += row;
    }
}
async function getAllGrades()
{
    var data = await fetch("http://localhost:5000/grades").then( r => r.text() );
    makeTable(data, "allGradeTable");
}

async function getSingleStudent()
{
    var name = document.querySelector("#getSingleName").value;
    var data = await fetch("http://localhost:5000/grades/" + name).then( r => r.ok ? r.text() : "no such student" );
    makeTable(data, "singleGradeTable");
}

async function postStudent()
{
    // {"name": "John Doe", "grade": 92.1}
    var postData = {"name": document.querySelector("#postSingleName").value, "grade": document.querySelector("#postSingleGrade").value};
    var data = await fetch('http://localhost:5000/grades', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify(postData),
        }
    ).then( r => r.ok ? r.text() : r.status == 409 ? "student already exists" : "bad json input" );
    // 409 => conflict of data, student already exists
    // otherwise they entered the wrong json ie {"name": "Jackie", "GRADE": 92.1}
    makeTable(data, "postGradeTable");
}

async function putStudent()
{
    // {"grade": 92.1}
    var name = document.querySelector("#putSingleName").value;
    var putData = {"grade": document.querySelector("#putSingleGrade").value};
    var data = await fetch('http://localhost:5000/grades/' + name, {
            method: 'PUT',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify(putData),
        }
    ).then( r => r.ok ? r.text() : r.status == 404 ? "student not found" : "bad json input" );
    // 404 => not found, student not found
    // otherwise they entered the wrong json ie {"GRADE": 92.1}
    makeTable(data, "putGradeTable");
}

async function deleteStudent()
{
    var name = document.querySelector("#deleteSingleName").value;
    var data = await fetch("http://localhost:5000/grades/" + name, {
            method: 'DELETE'
        }
    ).then( r => r.ok ? r.text() : "no such student" );
    makeTable(data, "deleteGradeTable");
}