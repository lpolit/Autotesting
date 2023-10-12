       <template>
         <div id="app">
           <div id="register">
             <div id="description">
               <img style="padding-top: 10px;" width="300" src="logo.png"/>
             </div>
             <div id="form">
               <form @submit.prevent="doChange">

                 <label for="email" style="margin-bottom: 20px">Email</label>
                 <input type="text" id="email" v-model="email" disabled style="color: gray">

                 <label for="password">Contraseña actual</label>&nbsp;
                 <i class="fas" :class="[passwordFieldIcon]" @click="hidePassword = !hidePassword"></i>
                 <input :type="passwordFieldType" id="password_act" v-model="password_act" placeholder="**********">


                 <label for="password">Contraseña</label>&nbsp;
                 <i class="fas" :class="[passwordFieldIcon]" @click="hidePassword = !hidePassword"></i>
                 <input :type="passwordFieldType" id="password" v-model="password" placeholder="**********">

                 <label for="confirm_password">Confirmar Contraseña</label>&nbsp;
                 <i class="fas" :class="[passwordFieldIcon]" @click="hidePassword = !hidePassword"></i>
                 <input :type="passwordFieldType" id="confirm_password" v-model="confirm_password" placeholder="**********">

                 <input style="color: red; font-size: 10px; border: none" id ="mensajeError" v-model="mensajeError"/>
                 <button class="btn" type="submit">Aceptar</button>
               </form>

             </div>
           </div>
         </div>
       </template>

       <script setup lang="ts">

       import router from "@/router";
       import {computed, onMounted, ref} from "vue";
       import axios from "axios";
       import { notify } from "@kyvg/vue3-notification";

       const email = ref(sessionStorage.getItem("user"));
       const hidePassword = ref(true);
       const password_act = ref("")
       const password = ref("");
       const confirm_password = ref("");
       const mensajeError = ref("");


       const passwordFieldIcon = computed(() => hidePassword.value ? "fa-eye" : "fa-eye-slash");
       const passwordFieldType = computed(() => hidePassword.value ? "password" : "text");

       onMounted (() => {
         localStorage.setItem("user", "")
       })

       const notificar = (type: string, title: string, text: string) =>{
         notify({
           type: type,
           title: title,
           text: text,
         });
       }


       const doChange = async () => {
         if (password.value == confirm_password.value){

             let json = {
               "email": email.value,
               "password_act": password_act.value,
               "password": password.value,
             }

             const path = '/api/user/change'
             await axios.post(path, json).then((response) => {
               notificar("success", "Operacion exitosa", "El cambio de la contraseña se realizo exitosamente")
               router.push("/")
             }).catch((error) => {
               notificar("error", "Fallo", error.response.data.detail)
               console.log(error)
             })
         }else{
           mensajeError.value="Las contraseñas deben coincidir"
         }
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

       div#app div#register {
         align-items: center;
         background-color: #e2e2e5;
         display: flex;
         justify-content: center;
         width: 100%;
         height: 100%;
       }

       div#app div#register div#description {
         background-color: #ffffff;
         width: 350px;
         padding: 35px;
         height: 250px;
       }

       div#app div#register div#description h1,
       div#app div#register div#description p {
         margin: 0;
       }

       div#app div#register div#description p {
         font-size: 0.8em;
         color: #95a5a6;
         margin-top: 10px;
       }

       div#app div#register div#form {
         background-color: #34495e;
         border-radius: 5px;
         box-shadow: 0px 0px 30px 0px #666;
         color: #ecf0f1;
         width: 300px;
         padding: 35px;
       }

       div#app div#register div#form label,
       div#app div#register div#form input {
         outline: none;
         width: 100%;
       }

       div#app div#register div#form label {
         color: #95a5a6;
         font-size: 0.8em;
       }

       div#app div#register div#form input {
         background-color: transparent;
         color: #ecf0f1;
         font-size: 1em;
         margin-bottom: 20px;
       }

       div#app div#register div#form ::placeholder {
         color: #ecf0f1;
         opacity: 1;
       }

       div#app div#register div#form button {
         background-color: #ffffff;
         cursor: pointer;
         border: none;
         padding: 10px;
         transition: background-color 0.2s ease-in-out;
         width: 100%;
       }

       div#app div#register div#form button:hover {
         background-color: #eeeeee;
       }

       @media screen and (max-width: 600px) {
         div#app div#register {
           align-items: unset;
           background-color: unset;
           display: unset;
           justify-content: unset;
         }

         div#app div#register div#description {
           margin: 0 auto;
           max-width: 350px;
           width: 100%;
         }

         div#app div#register div#form {
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


