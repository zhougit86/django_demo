/**
 * Created by zhouxg2 on 2016/12/21.
 */

'use strict';

angular.
module('guyApp').
config(function ($httpProvider){
    $httpProvider.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest';
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
}).
//config(function($interpolateProvider) {
//    $interpolateProvider.startSymbol('{$');
//    $interpolateProvider.endSymbol('$}');
//}).
component('guyList', {

    templateUrl: '/static/js/guy-list/guy-list.template.html',

    controller: function GuyController($http) {
        var self=this;
        self.orderProp = 'fields.age';
        self.user = {};


        $http.get('/api/guys/').then(function(response){
            self.guys= response.data;
        });

        self.Reset = function() {
            self.user={};
        };

        self.GuyCreate = function() {
           $http.post('/api/guys/',self.user)
        };
    }
});

