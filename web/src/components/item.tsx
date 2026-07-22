import { Check } from "lucide-preact";

export const Item = (props: { name: string; icon: string }) => {
  return (
    <label className="rounded-base shadow-shadow border-border bg-secondary-background text-foreground font-base flex flex-row items-center justify-between gap-2 border-2 p-4">
      <input
        type="checkbox"
        className="peer sr-only"
        // TODO this should be different so i can parse it back
        name={props.name}
      />
      <div>
        <img src={props.icon} className="size-8" />
        <span className="font-sans text-sm text-gray-900">{props.name}</span>
      </div>
      <Check className="text-main-foreground size-4" />
    </label>
  );
};
