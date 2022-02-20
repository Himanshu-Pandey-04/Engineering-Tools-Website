// Dict = 
//   {
//   'function_name': {
//       'docS': 'tooltip',
//       'params': [{
//           'p1': ['int', 'tooltip']
//       },
//       {
//         'p2': ['str', 'tooltip']
//       }
//     ],

//       'returns': {
//           'r1': ['list', 'tooltip']
//       },

//       'tags': ['tag1', 'tag2']
//   }
// }


// dataType = { 'int' : 'number', 'str' : 'text'}

// var ele = document.getElementById("demo");
// var code = '';

// for (let i=1 ; i<=Dict['function_name']['params'].length ; i++) {
//   dataT = Dict['function_name']['params'][i-1][`p${i}`][0];
//   code += `<input type='${dataType[dataT]}'/>`;
// }


// console.log(code);
// ele.innerHTML += code;

function DropDownToggle(key) {
  button = document.getElementById(`btn-${key}`);
  list = document.getElementById(`list-${key}`);
  if (list.style.display != 'none') list.style.display = 'none'; 
  else list.style.display = 'block';
}