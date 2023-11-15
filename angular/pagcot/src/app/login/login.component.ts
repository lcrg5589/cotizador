import { Component } from '@angular/core';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent {
  username: string = '';
  password: string = '';

  login() {
    // Aquí puedes agregar la lógica de autenticación, por ejemplo, haciendo una solicitud HTTP al servidor.
    console.log(`Usuario: ${this.username}, Contraseña: ${this.password}`);
  }
}
