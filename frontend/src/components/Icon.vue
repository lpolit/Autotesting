<script lang="ts">
import { computed, defineComponent, PropType, h } from "vue";

export default defineComponent({
  props: {
    id: { type: String, default: undefined },
    border: { type: Boolean, default: false },
    icon: { type: String },
    outlined: { type: Boolean, default: false },
  },
  setup(props) {

    const classes = computed(() => ({
      "material-icons": !props.outlined,
      "material-icons-outlined": props.outlined,
    }));

    const icon = h(
        "span",
        {
          class: ["icon", classes.value],
        },
        props.icon
    );

    if (props.border) {
      return () =>
          h(
              "span",
              {
                class: [
                  "icon-border border rounded-circle d-inline-flex overflow-hidden",
                  {

                  },
                ],
              },
              icon
          );
    }
    return () => icon;
  },
});
</script>

<style>
.icon-border {
  width: 36px;
  height: 36px;
}

.icon-border.icon-border-sm {
  width: 30px;
  height: 30px;
}

.icon-border.icon-border-lg {
  width: 58px;
  height: 58px;
}

.icon-border.icon-border-xl {
  width: 88px;
  height: 88px;
}
</style>
