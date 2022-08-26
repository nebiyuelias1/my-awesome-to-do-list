import jwt_decode from "jwt-decode";

export const isValidEmail = (email: string) => {
  const regexPattern =
    /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
  return regexPattern.test(email);
};

export const hasTokenExpired = () => {
    const token = localStorage.getItem('token');

    if (!token) {
        return true;
    }

    const decoded: any = jwt_decode(token);

    const expiration = new Date(decoded.exp * 1000);

    return expiration < new Date();
}
