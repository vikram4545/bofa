var myapp = angular.module("mymodule",[]);

myapp.controller("mycontroller",function($scope){

$scope.message = "hvgjhknjm"
});

myapp.config(function($interpolateProvider){
    $interpolateProvider.startSymbol("[[");
    $interpolateProvider.endSymbol("]]");
});
