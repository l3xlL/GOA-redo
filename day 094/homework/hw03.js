function updateUser(user, updates) {
    let updatedUser = {user};
    for (let update of updates) {
        updatedUser = {updatedUser, update};
    }
    return updatedUser;
}



let user = {name: "ana", age: 35, city: "madrid"};
let updates = [{age: 27}, {city: "barcelona"}, {name: "anna"}];
console.log(updateUser(user, updates));