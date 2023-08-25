<template>
  <div>
    <e-input v-model="filter" />
    {{ filter }}
    <e-table :items="items" :fields="fields" :filter="filter" :loading="loading">
      <template #cell(montoTotal)="data">
        <strong>{{ $filters.currency(data.unformatted, "$ ") }}</strong>
      </template>
      <template #card="{ item }">
        <div class="d-flex justify-content-between">
          <div>
            <div class="text-primary">Tique C</div>
            <div class="text-primary">{{ item.nroComprobante }}</div>
            <div>{{ item.razonSocial }}</div>
          </div>
          <div class="text-end">
            <h5 class="text-primary">{{ $filters.currency(item.montoTotal, "$ ") }}</h5>
            <div>{{ item.fechaEmision }}</div>
          </div>
        </div>
      </template>
    </e-table>
  </div>
</template>

<script setup lang="ts">
import { onMounted, ref } from "vue";
import type { TableField, TableItem } from "@eda/vue/src/types";

const filter = ref("");
const loading = ref(false);

interface Pagos {
  fechaEmision: string;
  tipo: string;
  nroComprobante: string;
  razonSocial: string;
  montoTotal: number;
}

onMounted(() => {
  loading.value = true;
  setTimeout(() => {
    items.value = [
      {
        fechaEmision: "20/04/2021",
        montoTotal: 312874.6539,
        nroComprobante: "6617412923",
        razonSocial: "Dore",
        tipo: "51a239fa-0e0f-43b9-b3b7-753954e28479",
      },
      {
        fechaEmision: "21/03/2021",
        montoTotal: 392011.5835,
        nroComprobante: "2126511529",
        razonSocial: "Avrit",
        tipo: "77aba5d5-1657-47c5-b3b2-9cad32389889",
      },
      {
        fechaEmision: "21/03/2021",
        montoTotal: 392011.5835,
        nroComprobante: "2126511529",
        razonSocial: "Avrit",
        tipo: "77aba5d5-1657-47c5-b3b2-9cad32389889",
      },
      {
        fechaEmision: "21/03/2021",
        montoTotal: 392011.5835,
        nroComprobante: "2126511529",
        razonSocial: "Avrit",
        tipo: "77aba5d5-1657-47c5-b3b2-9cad32389889",
      },
      {
        fechaEmision: "28/02/2021",
        montoTotal: 394257.9894,
        nroComprobante: "4483683713",
        razonSocial: "Wilt",
        tipo: "b95461a9-f68a-4987-80a8-9e89b1fa6ecf",
      },
      {
        fechaEmision: "16/04/2021",
        montoTotal: 314500.2697,
        nroComprobante: "4641051003",
        razonSocial: "Wang",
        tipo: "99232286-e6ff-451c-8625-f8b533dd6841",
      },
      {
        fechaEmision: "16/11/2021",
        montoTotal: 248128.8874,
        nroComprobante: "9354114377",
        razonSocial: "Phyllida",
        tipo: "f1dd7945-6619-4569-b26f-1078696231b5",
      },
      {
        fechaEmision: "08/03/2021",
        montoTotal: 171097.3691,
        nroComprobante: "5226860560",
        razonSocial: "Claude",
        tipo: "046664c9-ddc1-4aee-abe4-64edd01f2899",
      },
      {
        fechaEmision: "02/05/2021",
        montoTotal: 387898.0182,
        nroComprobante: "1138545392",
        razonSocial: "Aron",
        tipo: "64b50155-80d1-434e-a4b5-2ff81e4ef17d",
      },
      {
        fechaEmision: "28/10/2021",
        montoTotal: 359503.3248,
        nroComprobante: "6135964216",
        razonSocial: "Garnet",
        tipo: "98970015-dab0-4717-bb38-bc96da4d7030",
      },
      {
        fechaEmision: "17/10/2021",
        montoTotal: 395679.211,
        nroComprobante: "8152341177",
        razonSocial: "Carol-jean",
        tipo: "a8979d02-841d-4d5c-943d-468fe7d65c12",
      },
      {
        fechaEmision: "12/09/2021",
        montoTotal: 193370.1649,
        nroComprobante: "9086073808",
        razonSocial: "Joane",
        tipo: "e0134f85-aaff-4b2e-9625-a7a71c8111ca",
      },
      {
        fechaEmision: "10/10/2021",
        montoTotal: 268434.5378,
        nroComprobante: "6940954538",
        razonSocial: "Tony",
        tipo: "f10ef9f5-dacc-4c1a-bb69-7b7b427b9a7f",
      },
      {
        fechaEmision: "10/11/2021",
        montoTotal: 246400.5928,
        nroComprobante: "1236538404",
        razonSocial: "Daryle",
        tipo: "1dee4e2b-21cd-459a-a5ea-4c88edee248b",
      },
      {
        fechaEmision: "16/10/2021",
        montoTotal: 482089.9077,
        nroComprobante: "1189836637",
        razonSocial: "Shayla",
        tipo: "bd34b217-a2db-4164-8439-e3afea62e98f",
      },
      {
        fechaEmision: "06/11/2021",
        montoTotal: 264647.9887,
        nroComprobante: "7033369638",
        razonSocial: "Karalynn",
        tipo: "5957aaa7-45d6-4861-81f5-9a87ab52d19d",
      },
      {
        fechaEmision: "22/11/2021",
        montoTotal: 324985.7996,
        nroComprobante: "1177494477",
        razonSocial: "Brnaba",
        tipo: "b84d4229-9c31-4d1a-b684-698f545dbff8",
      },
      {
        fechaEmision: "19/08/2021",
        montoTotal: 367303.9165,
        nroComprobante: "8009107743",
        razonSocial: "Liz",
        tipo: "4ea77702-00f6-477e-8058-a46f8a979ae4",
      },
      {
        fechaEmision: "24/01/2022",
        montoTotal: 447224.9238,
        nroComprobante: "2631355423",
        razonSocial: "Sisile",
        tipo: "b866ba89-affc-48b2-a8d1-e8563f867294",
      },
      {
        fechaEmision: "14/11/2021",
        montoTotal: 294489.3775,
        nroComprobante: "6149761967",
        razonSocial: "Lainey",
        tipo: "431e23a3-f6ad-4068-b452-c048d7e31964",
      },
      {
        fechaEmision: "27/06/2021",
        montoTotal: 338713.2987,
        nroComprobante: "5389888871",
        razonSocial: "Rhianon",
        tipo: "790700b0-eb00-4aa0-adbe-9c54006dd99b",
      },
      {
        fechaEmision: "06/11/2021",
        montoTotal: 406000.9317,
        nroComprobante: "7245662843",
        razonSocial: "Bradley",
        tipo: "f16ff08f-29af-46c9-9de8-05da866670bf",
      },
      {
        fechaEmision: "27/05/2021",
        montoTotal: 170779.3337,
        nroComprobante: "1342402510",
        razonSocial: "Kiley",
        tipo: "8d64d52d-7dbe-4027-ad38-5ddbd6d80576",
      },
      {
        fechaEmision: "26/02/2021",
        montoTotal: 470658.975,
        nroComprobante: "5220947370",
        razonSocial: "Kenton",
        tipo: "c294c2dc-6207-4b32-9d06-bb1378bc6b95",
      },
      {
        fechaEmision: "23/07/2021",
        montoTotal: 266023.4829,
        nroComprobante: "6948799396",
        razonSocial: "Quinn",
        tipo: "975d4985-02be-43bf-9619-b71325953826",
      },
      {
        fechaEmision: "01/06/2021",
        montoTotal: 497597.7872,
        nroComprobante: "5548311832",
        razonSocial: "Culver",
        tipo: "9ed1d9bf-c299-498f-92de-227633aa978e",
      },
      {
        fechaEmision: "27/10/2021",
        montoTotal: 273694.0912,
        nroComprobante: "9084035534",
        razonSocial: "Veda",
        tipo: "7a5ebb4f-8493-47f8-8970-c70fc1b1e1fd",
      },
      {
        fechaEmision: "27/04/2021",
        montoTotal: 292734.4618,
        nroComprobante: "5658536480",
        razonSocial: "Oliviero",
        tipo: "76855a01-737c-4ff5-ba5a-f2b858e0083f",
      },
      {
        fechaEmision: "01/06/2021",
        montoTotal: 277796.5104,
        nroComprobante: "1027368662",
        razonSocial: "Torey",
        tipo: "213b167e-a40e-489d-8668-961282c0fddb",
      },
      {
        fechaEmision: "17/10/2021",
        montoTotal: 322497.3318,
        nroComprobante: "8282252484",
        razonSocial: "Gage",
        tipo: "ebc90e04-5b73-4fc1-b9a2-28549e3eed0f",
      },
      {
        fechaEmision: "29/12/2021",
        montoTotal: 264855.8977,
        nroComprobante: "8750653040",
        razonSocial: "Odo",
        tipo: "dcf7e50c-61c0-468c-99fd-41e151c13e2d",
      },
      {
        fechaEmision: "23/11/2021",
        montoTotal: 394928.8423,
        nroComprobante: "7299540363",
        razonSocial: "De",
        tipo: "0804f097-93ce-4c08-b1b7-4e96a2fe0050",
      },
    ];
    loading.value = false;
  }, 1000);
});

const items = ref<TableItem<Pagos>[]>([]);
const fields = ref<TableField<Pagos>[]>([
  {
    key: "fechaEmision",
    label: "Fecha de emisión",
  },
  {
    key: "montoTotal",
    formatter: (value) => `$ ${value}`,
    class: "text-end text-nowrap fvn-tabular-nums",
  },
  { key: "nroComprobante", label: "N° de comprobante", variant: "primary" },
  { key: "razonSocial", label: "Nombre o razón social" },
]);

</script>
