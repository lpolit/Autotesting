       <template>
         <div id="app">
           <div id="login">
             <div id="description">
               <img width="300" src="logo.png"/>
               <p style="width:311px">
                 <b>Automatizacion al alcance de todos!</b> <br>
                 Consiga mayor cobertura con menor esfuerzo, agilizando las pruebas repetitivas.
               </p>
             </div>
             <div id="form">
               <form @submit.prevent="doLogin">
                 <label for="email" style="margin-bottom: 20px">Email</label>
                 <input type="text" id="email" v-model="email" placeholder="mail@example.com" autocomplete="off">

                 <label for="password">Contraseña</label>&nbsp;
                 <i class="fas" :class="[passwordFieldIcon]" @click="hidePassword = !hidePassword"></i>
                 <input :type="passwordFieldType" id="password" v-model="password" placeholder="**********">
                 <input style="color: red; font-size: 10px; border: none" id ="mensajeError" v-model="mensajeError"/>
                 <button class="btn" type="submit">Ingresar</button>
               </form>
               <div class="col-5 mx-auto"  >
                 <button  @click="go_register" style="margin-top: 15px; color:black; padding: 2px; font-size:12px" >
                   Register
                 </button>

               </div>
               <a @click="reset" class="btn btn-link" style="font-size: 12px; margin: 18px 0 0 13px">
                 Olvido su Contraseña?
               </a>
             </div>
           </div>
         </div>
       </template>

       <script setup>

       import router from "@/router";
       import {computed, onMounted, ref} from "vue";
       import axios from "axios";


       const email = ref("");
       const hidePassword = ref(true);
       const password = ref("");
       const mensajeError = ref("");

       const passwordFieldIcon = computed(() => hidePassword.value ? "fa-eye" : "fa-eye-slash");
       const passwordFieldType = computed(() => hidePassword.value ? "password" : "text");

       onMounted (() => {
         localStorage.setItem("user", "")
       })

       const go_register = () => {
         router.push("register")
       }
       const reset = () => {
         router.push("reset")
       }

       const doLogin = async () => {

         let json = {
           "email": email.value,
           "password": password.value
         }

         const path = '/api/user/login'
         await axios.post(path, json).then((response) => {
           sessionStorage.setItem("user", email.value);
           sessionStorage.setItem("Authorization",response.data["access token"])
           router.push("home_project")
         }).catch((error) => {
           mensajeError.value = "Usuario o clave Invalida"
           console.log(error)
         })
       }


       </script>

       <style>
       * {
         box-sizing: border-box;
         font-family: Verdana, sans-serif;
       }

       html,
       body {
         height: 100%;
         margin: 0;
         padding: 0;
         width: 100%;
       }

       div#app {
         width: 100%;
         height: 100%;
       }

       div#app div#login {
         align-items: center;
         background-color: #e2e2e5;
         display: flex;
         justify-content: center;
         width: 100%;
         height: 100%;
       }

       div#app div#login div#description {
         background-color: #ffffff;
         width: 350px;
         padding: 35px;
         height: 250px;
       }

       div#app div#login div#description h1,
       div#app div#login div#description p {
         margin: 0;
       }

       div#app div#login div#description p {
         font-size: 0.8em;
         color: #95a5a6;
         margin-top: 10px;
       }

       div#app div#login div#form {
         background-color: #34495e;
         border-radius: 5px;
         box-shadow: 0px 0px 30px 0px #666;
         color: #ecf0f1;
         width: 300px;
         padding: 35px;
       }

       div#app div#login div#form label,
       div#app div#login div#form input {
         outline: none;
         width: 100%;
       }

       div#app div#login div#form label {
         color: #95a5a6;
         font-size: 0.8em;
       }

       div#app div#login div#form input {
         background-color: transparent;
         color: #ecf0f1;
         font-size: 1em;
         margin-bottom: 20px;
       }

       div#app div#login div#form ::placeholder {
         color: #ecf0f1;
         opacity: 1;
       }

       div#app div#login div#form button {
         background-color: #ffffff;
         cursor: pointer;
         border: none;
         padding: 10px;
         transition: background-color 0.2s ease-in-out;
         width: 100%;
       }

       div#app div#login div#form button:hover {
         background-color: #eeeeee;
         color: dimgray;
       }

       @media screen and (max-width: 600px) {
         div#app div#login {
           align-items: unset;
           background-color: unset;
           display: unset;
           justify-content: unset;
         }

         div#app div#login div#description {
           margin: 0 auto;
           max-width: 350px;
           width: 100%;
         }

         div#app div#login div#form {
           border-radius: unset;
           box-shadow: unset;
           width: 100%;
         }

         div#app div#login div#form form {
           margin: 0 auto;
           max-width: 280px;
           width: 100%;
         }


       }
       </style>


