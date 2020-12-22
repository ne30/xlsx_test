import React,{Component} from 'react'; 
  
class App extends Component { 

    state = { 
      selectedFile: null
    }; 
     
    onFileChange = event => { 
      this.setState({ selectedFile: event.target.files[0] }); 
     
    }; 
    

    onTask1 = () => { 
     
      // Create an object of formData 
      console.log(this.state.selectedFile); 
        
      var formdata = new FormData();
      formdata.append("file", this.state.selectedFile, this.state.selectedFile.name);

      var requestOptions = {
        method: 'POST',
        body: formdata,
        redirect: 'follow'
      };

      fetch("http://localhost:8000/file/upload/", requestOptions)
        .then(response => response.text())
        .then(result => console.log(result))
        .catch(error => console.log('error', error));
      
        setTimeout(() => {
          const response = {
            file: 'http://localhost:8000/media/task1.xlsx',
          };
          // server sent the url to the file!
          // now, let's download:
          window.location.href = response.file;
        }, 5000);
    }; 

    onTask2 = () => { 
     
      console.log(this.state.selectedFile); 
        
      var formdata = new FormData();
      formdata.append("file", this.state.selectedFile, this.state.selectedFile.name);

      var requestOptions = {
        method: 'POST',
        body: formdata,
        redirect: 'follow'
      };
      fetch("http://localhost:8000/file/roundoff/", requestOptions)
        .then(response => response.text())
        .then(result => console.log(result))
        .catch(error => console.log('error', error));
        setTimeout(() => {
          const response = {
            file: 'http://localhost:8000/media/task2.xlsx',
          };
          // server sent the url to the file!
          // now, let's download:
          window.location.href = response.file;
        }, 5000);
    }; 
    
    onTask3 = () => { 
     
      console.log(this.state.selectedFile); 
        
      var formdata = new FormData();
      formdata.append("file", this.state.selectedFile, this.state.selectedFile.name);

      var requestOptions = {
        method: 'POST',
        body: formdata,
        redirect: 'follow'
      };

      fetch("http://localhost:8000/file/mean/", requestOptions)
        .then(response => response.text())
        .then(result => console.log(result))
        .catch(error => console.log('error', error));
      
        setTimeout(() => {
          var response = {
            file: 'http://localhost:8000/media/task3.xlsx',
          };
          // server sent the url to the file!
          // now, let's download:
          window.location.href = response.file;
        }, 5000);

    }; 

     
    fileData = () => { 
     
      if (this.state.selectedFile) { 
          
        return ( 
          <div> 
            <h2>File Details:</h2> 
            <p>File Name: {this.state.selectedFile.name}</p> 
            <p>File Type: {this.state.selectedFile.type}</p> 
          </div> 
        ); 
      } else { 
        return ( 
          <div> 
            <br /> 
            <h4>Choose before Pressing the buttons!</h4> 
          </div> 
        ); 
      } 
    }; 
     
    render() { 
     
      return ( 
        <div> 
            <h1> 
              Xlsx Test
            </h1> 
            <h3> 
              File Upload! 
            </h3> 
            <div> 
                <input type="file" onChange={this.onFileChange} /> 
                <button onClick={this.onTask1}> 
                  Task1! 
                </button> 
                <button onClick={this.onTask2}> 
                  Task2! 
                </button>
                <button onClick={this.onTask3}> 
                  Task3! 
                </button>
            </div> 
          {this.fileData()} 
        </div> 
      ); 
    } 
  } 
  
  export default App; 
