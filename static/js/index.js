Dict = 
  {
  'function_name': {
      'docS': 'tooltip',
      'params': [{
          'p1': ['int', 'tooltip']
      },
      {
        'p2': ['str', 'tooltip']
      }
    ],

      'returns': {
          'r1': ['list', 'tooltip']
      },

      'tags': ['tag1', 'tag2']
  }
}


dataType = { 'int' : 'number', 'str' : 'text'}

var ele = document.getElementById("demo");
var code = '';

for (let i=1 ; i<=Dict['function_name']['params'].length ; i++) {
  dataT = Dict['function_name']['params'][i-1][`p${i}`][0];
  code += `<input type='${dataType[dataT]}'/>`;
}


console.log(code);
ele.innerHTML += code;