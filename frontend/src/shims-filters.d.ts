//file added

import Filters from "./types/Filters";

declare module "@vue/runtime-core" {
  interface ComponentCustomProperties {
    $filters: Filters;
  }
}
