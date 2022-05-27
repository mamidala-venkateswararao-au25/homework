


const initialState = "#000000"

const modifyColor = (colorState = initialState, action) => {

    switch (action.type) {
        case "CHANGE COLOR":
            function generateRandomColor() {
                var letters = '0123456789ABCDEF';
                var color = '#';
                for (var i = 0; i < 6; i++) {
                  color += letters[Math.floor(Math.random() * 16)];
                }
                return color;
              }
              
            var randomColor=generateRandomColor();

            return randomColor
            
    
        default:
            return colorState
    }
}

export {modifyColor}