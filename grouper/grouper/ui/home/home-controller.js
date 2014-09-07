bling.home.controller('HomeCtrl', ['$scope', '$http', function($scope, $http){
    $scope.home = new function(){
        var private = {
            generateGroups: function(){
                $http({method: 'GET', url: 'api/groups', params: {
                        members: public.members,
                        illegalPairs: public.illegalPairs,
                        groupSize: public.groupSize             
                    }
                })
                .success(function(data){
                    public.groups = data
                })
            }
        }
        
        var public = {          
            generateGroups: private.generateGroups,            
            
            members: [],
            illegalPairs: [],
            groupSize: 5,
            
            addMember: function(){
                this.members.push({name: ''} )
            }
        }
        
        names = ['Liam', 'Olivia', 
                'Noah', 'Emma', 
                'Ethan', 'Sophia' ,
                'Mason' ,'Ava',               
                'Logan',    'Isabella',             
                'Lucas',    'Mia',              
                'Jacob',    'Charlotte',                
                'Jackson',  'Emily',                
                'Jack', 'Harper',               
                'Aiden',    'Abigail',              
                'Elijah',   'Avery']
        
        for (i in names){
            public.members.push({name: names[i]})
        }

        
        return public
    }
}])