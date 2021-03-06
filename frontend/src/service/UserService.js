import UserType from "./UserType";

const USER_LOCAL_KEY = "current_user";

export function saveUser(user) {
    localStorage.setItem(USER_LOCAL_KEY, JSON.stringify(user));
}

export function loadUser() {
    const user = localStorage.getItem(USER_LOCAL_KEY);
    return JSON.parse(user);
}

export function getUserType() {
    const user = loadUser();
    if (!user) {
        return null;
    }
    return user.cnpj ? UserType.store : UserType.user;
}
