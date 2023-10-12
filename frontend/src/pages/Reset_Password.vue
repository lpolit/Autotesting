       <template>
         <div id="app">
           <div id="reset_password">
             <div id="description">
               <img style="padding-top: 10px;" width="300" src="logo.png"/>
             </div>
             <div id="form">
               <form @submit.prevent="doReset">


                 <h5>Recuperar contraseña</h5>
                 <label style="color: cadetblue; margin-bottom: 50px">Ingresar el correo electronico para recuperar tu contraseña</label>

                 <label for="email" style="margin-bottom: 20px">Email</label>
                 <input type="text" id="email" v-model="email" placeholder="mail@example.com" autocomplete="off">



                 <button class="btn" type="submit">Resetar contraseña</button>
               </form>
               <a href="#" class="btn btn-link" style="font-size: 12px; margin-top: 15px;">
                 Volver
               </a>
             </div>
           </div>
         </div>
       </template>


 <script setup lang="ts">


 import { notify } from "@kyvg/vue3-notification";
 import {computed, onMounted, ref} from "vue";
 import axios from "axios";

 const email = ref("");
 const notificar = (type: string, title: string, text: string) =>{
   notify({
     type: type,
     title: title,
     text: text,
   });
 }
 onMounted (() => {
   localStorage.setItem("user", "")
 })



 const doReset = async () => {

   const path = '/api/user/reset/'+email.value
   await axios.post(path).then((response) => {

     notificar("success", "Operacion exitosa", "El blanqueo del usuario "+ response.data+" la contraseña se realizo exitosamente")

   }).catch((error) => {
      notificar("error", "Fallo", "Fallo el blanqueo de la contraseña!")   })
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

 div#app div#reset_password {
   align-items: center;
   background-color: #e2e2e5;
   display: flex;
   justify-content: center;
   width: 100%;
   height: 100%;
 }

 div#app div#reset_password div#description {
   background-color: #ffffff;
   width: 350px;
   padding: 35px;
   height: 250px;
 }

 div#app div#reset_password div#description h1,
 div#app div#reset_password div#description p {
   margin: 0;
 }

 div#app div#reset_password div#description p {
   font-size: 0.8em;
   color: #95a5a6;
   margin-top: 10px;
 }

 div#app div#reset_password div#form {
   background-color: #34495e;
   border-radius: 5px;
   box-shadow: 0px 0px 30px 0px #666;
   color: #ecf0f1;
   width: 350px;
   padding: 35px;
 }

 div#app div#reset_password div#form label,
 div#app div#reset_password div#form input {
   outline: none;
   width: 100%;
 }

 div#app div#reset_password div#form label {
   color: #95a5a6;
   font-size: 0.8em;
 }

 div#app div#reset_password div#form input {
   background-color: darkgray;
   color: #ecf0f1;
   font-size: 1em;
   margin-bottom: 20px;
 }

 div#app div#reset_password div#form ::placeholder {
   color: #ecf0f1;
   opacity: 1;
 }

 div#app div#reset_password div#form button {
   background-color: #ffffff;
   cursor: pointer;
   border: none;
   padding: 10px;
   transition: background-color 0.2s ease-in-out;
   width: 100%;
 }

 div#app div#reset_password div#form button:hover {
   background-color: #eeeeee;
 }

 @media screen and (max-width: 600px) {
   div#app div#reset_password {
     align-items: unset;
     background-color: unset;
     display: unset;
     justify-content: unset;
   }

   div#app div#reset_password div#description {
     margin: 0 auto;
     max-width: 350px;
     width: 100%;
   }

   div#app div#reset_password div#form {
     border-radius: unset;
     box-shadow: unset;
     width: 100%;
   }

   div#app div#reset_password div#form form {
     margin: 0 auto;
     max-width: 280px;
     width: 100%;
   }


 }
 </style>


