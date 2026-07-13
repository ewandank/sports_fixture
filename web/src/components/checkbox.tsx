import { Check } from "lucide-preact";
import type { ComponentProps } from "preact";

// Using ComponentProps ensures you target the native element attributes cleanly

export function Checkbox({ className, ...props }: ComponentProps<"input">) {
  return (
    <div className="relative flex items-center justify-center size-4 shrink-0">
      <input
        type="checkbox"
        className="peer size-4 appearance-none rounded-sm outline-2 outline-border ring-offset-white focus-visible:outline-hidden focus-visible:ring-2 focus-visible:ring-black focus-visible:ring-offset-2 disabled:cursor-not-allowed disabled:opacity-50 checked:bg-main checked:text-white"
        {...props}
      />
      <div
        data-slot="checkbox-indicator"
        className="pointer-events-none absolute hidden peer-checked:flex items-center justify-center text-current"
      >
        <Check className="size-4 text-main-foreground" />
      </div>
    </div>
  );
}
