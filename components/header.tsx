import { Button } from "@/components/ui/button"
import { Hand } from "lucide-react"

export function Header() {
  return (
    <header className="fixed top-0 left-0 right-0 z-50 bg-background/90 backdrop-blur-xl border-b border-border/60 shadow-sm">
      <div className="container mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex items-center justify-between h-20">
          <div className="flex items-center gap-3">
            <div className="flex items-center justify-center w-11 h-11 rounded-xl bg-gradient-to-br from-primary to-secondary shadow-md">
              <Hand className="w-6 h-6 text-primary-foreground" aria-hidden="true" />
            </div>
            <span className="text-xl font-semibold tracking-tight text-foreground">SignCast</span>
          </div>

          <nav className="hidden md:flex items-center gap-10">
            <a
              href="#features"
              className="text-sm font-medium text-muted-foreground hover:text-foreground transition-colors duration-200"
            >
              Features
            </a>
            <a
              href="#how-it-works"
              className="text-sm font-medium text-muted-foreground hover:text-foreground transition-colors duration-200"
            >
              How It Works
            </a>
            <a
              href="#demo"
              className="text-sm font-medium text-muted-foreground hover:text-foreground transition-colors duration-200"
            >
              Demo
            </a>
          </nav>

          <div className="flex items-center gap-3">
            <Button
              size="sm"
              className="bg-gradient-to-r from-primary to-secondary hover:shadow-lg transition-all duration-200"
            >
              Get Started
            </Button>
          </div>
        </div>
      </div>
    </header>
  )
}
