document.addEventListener('DOMContentLoaded', function() {
  const input = document.getElementById("inputId");

  let query = ""

  if (input) {
    input.addEventListener("input", function() {
       query = input.value;
      console.log('Query:', query);
    })}  else {
      console.error(" No input");
    }

      const button = document.getElementById("SubmitButton");
      if (button) {
        button.addEventListener("click", function() {
        console.log("button is clicked")
          fetch(`http://127.0.0.1:5000/api/search?query=${query}`, {
            mode: "cors"})
            .then(response => response.json())
            .then(data => {
              const summary = data.summary;
              const output = document.getElementById("output");
              output.innerText = summary;
              console.log(data)
            })
            .catch(error => {
              console.error("Error", error);
            });
        });
      }
    });