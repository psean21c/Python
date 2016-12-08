// Written by YeoJin Yoon on Dec-8-2016
// How to call the function 
// calculate(1,2,3,4) 
// calculate(1,2,3,4,5,6,7) 

function calculate(){
    function createArrayUntilPassNumber(number){
        var rtn = [];
        for(var i = 0; i <= number; i++)
            rtn.push(i);
        return rtn;
    }

    function combineTwoArrayToOnePossibleCombination(arr1, arr2) {
        var rtn = [];

        if(arr1.length == 0)
            return arr2;

        for(var i = 0; i < arr1.length; i++){
            for(var j = 0; j < arr2.length; j++){
                if(arr1[i].constructor === Array){
                    rtn.push(arr1[i].concat(arr2[j]));
                }
                else
                    rtn.push([arr1[i], arr2[j]]);
            }
        }

        return rtn;
    }

    var tmp = [];
    var passingNumberCount = arguments.length;
    var lastValue = arguments[arguments.length - 1];
    for(var n = 0; n < passingNumberCount - 1; n++){
        tmp.push(createArrayUntilPassNumber(arguments[n]));
    }

    var newTmp = tmp.reduce((a, b) => {
        return combineTwoArrayToOnePossibleCombination(a, b);
    },[]);

    var answer = newTmp.filter((i) => i.reduce((a,b) => a + b, 0) != lastValue);

    console.log('answer', answer);
}
