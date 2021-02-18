<template>
   <div class="container">
        <div class="row">
            <div class="col text-left">
                <h2 class="mb-4">Nuevo Libro</h2>
            </div>
        </div>

        <div class="row">
            <div class="col">
                <div class="card">
                    <div class="card-body">
                        <form @submit="onSubmit">

                            <div class="form-group row">
                               <label for="title" class="col-sm-2 col-form-label">Título</label>
                               <div class="col-sm-6">
                                   <input type="text" placeholder="Título" name="title" class="form-control" v-model.trim="form.title">
                                </div> 
                            </div>

                            <div class="form-group row">
                               <label for="description" class="col-sm-2 col-form-label">Título</label>
                               <div class="col-sm-6">
                                   <textarea name="description" class="form-control" placeholder="Descripción" rows="8" cols="80" v-model.trim="form.description"></textarea>
                                </div> 
                            </div>

                            <div class="rows">
                                <div class="col text-left">
                                    <b-button type="submit" variant="primary">Crear</b-button>
                                    <b-button type="submit" class="btn-large-space" :to="{ name: 'ListBook' }">Cancelar</b-button>
                                </div>
                            </div>
                        </form>   
                    </div>
                </div>
            </div>
        </div>

    </div> 
</template>

<script>

import axios from 'axios';
import Swal from 'sweetalert2'

export default {
  
    data() {

        return {

            
            form: {
                title: '',
                description: ''
            }
        }
    },
    methods: {
        async onSubmit(evt) {

            evt.preventDefault();

            const path = `http://localhost:8000/api/v1.0/books/`;

            axios.post(path, this.form).then( resp => {

                this.form.title = resp.data.title;
                this.form.description = resp.data.description;

                Swal.fire({
                    position: 'top-end',
                    icon: 'success',
                    title: 'Libro creado correctamente',
                    showConfirmButton: false,
                    timer: 1500
                  })
                
                setTimeout(() => {
                    location.href = '/books';    
                }, 1500);
            })
            .catch( error => {
                
                Swal.fire({
                    icon: 'error',
                    title: 'Error ',
                    text: 'Algo salió mal, vuelve a intentar',
                  })
            })
        },

    }
  
}
</script>