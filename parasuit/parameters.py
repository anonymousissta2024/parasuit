class KLEEParameters:
    def __init__(self):
        self.boolean_parameters = [
            ["-strip-all", "false"],
            ["-strip-debug", "false"],
            ["-use-merge", "false"],
            ["-watchdog", "false"],
            ["-allocate-determ", "false"],
            ["-output-istats", "true"],
            ["-output-stats", "true"],
            ["-output-module", "false"],
            ["-compress-query-log", "false"],
            ["-check-div-zero", "true"],
            ["-write-paths", "false"],
            ["-write-no-tests", "false"],
            ["-use-branch-cache", "true"],
            ["-use-visitor-hash", "true"],
            ["-pc-all-widths", "false"],
            ["-pc-prefix-width", "true"],
            ["-only-seed", "false"],
            ["-all-external-warnings", "false"],
            ["-debug-cex-cache-check-binding", "false"],
            ["-debug-check-for-implied-values", "false"],
            ["-return-null-on-zero-malloc", "false"],
            ["-suppress-external-warnings", "false"],
            ["-exit-on-error", "false"],
            ["-dump-states-on-halt", "true"],
            ["-use-incomplete-merge", "false"],
            ["-track-instruction-time", "false"],
            ["-use-independent-solver", "true"],
            ["-debug-dump-stp-queries", "false"],
            ["-debug-log-merge", "false"],
            ["-debug-print-escaping-functions", "false"],
            ["-debug-validate-solver", "false"],
            ["-log-partial-queries-early", "false"],
            ["-log-timed-out-queries", "true"],
            ["-pc-width-as-arg", "true"],
            ["-use-construct-hash-stp", "true"],
            ["-warn-all-external-symbols", "false"],
            ["-always-output-seeds", "true"],
            ["-cex-cache-exp", "false"],
            ["-cex-cache-superset", "false"],
            ["-const-array-opt", "false"],
            ["-emit-all-errors", "false"],
            ["-klee-call-optimisation", "true"],
            ["-readable-posix-inputs", "false"],
            ["-use-batching-search", "false"],
            ["-use-constant-arrays", "true"],
            ["-debug-compress-instructions", "false"],
            ["-named-seed-matching", "false"],
            ["-only-replay-seeds", "false"],
            ["-pc-multibyte-reads", "true"],
            ["-silent-klee-assume", "false"],
            ["-smtlib-human-readable", "false"],
            ["-solver-optimize-divides", "false"],
            ["-write-test-info", "false"],
            ["-zero-seed-extension", "false"],
            ["-replay-keep-symbolic", "false"],
            ["-ignore-solver-failures", "false"],
            ["-pc-all-const-widths", "false"],
            ["-equality-substitution", "true"],
            ["-check-overshift", "true"],
            ["-disable-internalize", "false"],
            ["-disable-verify", "false"],
            ["-output-source", "true"],
            ["-rewrite-equalities", "true"],
            ["-use-call-paths", "true"],
            ["-use-cex-cache", "true"],
            ["-use-forked-solver", "true"],
            ["-verify-each", "false"],
            ["-write-kqueries", "false"],
            ["-simplify-sym-indices", "false"],
            ["-max-memory-inhibit", "true"],
            ["-write-smt2s", "false"],
            ["-write-sym-paths", "false"],
            ["-write-cvcs", "false"],
            ["-write-cov", "false"],
            ["-cex-cache-try-all", "false"],
            ["-debug-assignment-validating-solver", "false"],
            ["-debug-log-incomplete-merge", "false"],
            ["-debug-log-state-merge", "false"],
            ["-use-fast-cex-solver", "false"],
            ["-warnings-only-to-file", "false"],
            ["-use-iterative-deepening-time-search", "false"],
            ["-make-concrete-symbolic", 0],

            ["-posix-runtime", "false"],
            ["-only-output-states-covering-new", "false"],
            ["-optimize", "false"],
            ["-allow-seed-extension", "false"],
            ["-allow-seed-truncation", "false"],
            ["-disable-inlining", "false"]
        ]

        self.integer_parameters = [
            ["-max-memory", 2000, None],
            ["-max-sym-array-size", 0, 0],
            ["-max-depth", 0, 0],
            ["-allocate-determ-size", 100, None],
            ["-batch-instructions", 10000, None],
            ["-max-forks", 4294967295, 4294967295],
            ["-max-stack-frames", 8192, 0],
            ["-redzone-size", 10, None],
            ["-stats-commit-after", 0, 0],
            ["-stats-write-after-instructions", 0, 0],
            ["-istats-write-after-instructions", 0, 0],
            ["-max-tests", 0, 0],
            ["-max-instructions", 0, 0]
        ]

        self.float_parameters = [
            ["-max-static-fork-pct", 1.0, None],
            ["-max-static-solve-pct", 1.0, None],
            ["-max-static-cpfork-pct", 1.0, None],
            ["-max-static-cpsolve-pct", 1.0, None],
            ["-array-value-ratio", 1.0, None],
            ["-array-value-symb-ratio", 1.0, None]
        ]

        self.stringTime_parameters = [
            ["-timer-interval", "1s", None],
            ["-batch-time", "5s", "0s"],
            ["-max-solver-time", "0s", "0s"],
            ["-min-query-time-to-log", "0s", "0s"],
            ["-seed-time", "0s", "0s"],
            ["-uncovered-update-interval", "30s", None],
            ["-stats-write-interval", "1s", None],
            ["-istats-write-interval", "10s", None]
        ]

        self.string_parameters = [
            ["-external-calls", "concrete", ["concrete", "all", "none"]],
            ["-search", "random-path",
             ["dfs", "bfs", "random-state", "random-path", "nurs:covnew", "nurs:md2u", "nurs:depth", "nurs:rp",
              "nurs:icnt", "nurs:cpicnt", "nurs:qc"]],
            ["-switch-type", "internal", ["internal", "simple", "llvm"]],
            ["-smtlib-abbreviation-mode", "let", ["none", "let", "named"]],
            ["-smtlib-display-constants", "dec", ["bin", "hex", "dec"]],
            ["-use-query-log", None, [None, "all:kquery", "all:smt2", "solver:kquery", "solver:smt2"]],
            ["-optimize-array", None, [None, "all", "index", "value"]],
            ["-solver-backend", "stp", ["stp", "metasmt", "dummy", "z3"]],
            ["-debug-crosscheck-core-solver", "none", ["none", "stp", "metasmt", "dummy", "z3"]],
            ["-libc", "none", ["none", "klee", "uclibc"]]
        ]

        self.totalParams = self.boolean_parameters + self.integer_parameters + self.float_parameters + self.stringTime_parameters + self.string_parameters


        self.description = {
            '-strip-all': "Strip all symbol information from executable", 
            '-strip-debug': "Strip debugger symbol info from executable", 
            '-use-merge': "Enable support for path merging via klee_open_merge() and klee_close_merge()", 
            '-watchdog': "Use a watchdog process to enforce --max-time.", 
            '-allocate-determ': "Allocate memory deterministically", 
            '-output-istats': "Write instruction level statistics in callgrind format", 
            '-output-stats': "Write running stats trace file", 
            '-output-module': "Write the bitcode for the final transformed module", 
            '-compress-query-log': "Compress query log files", 
            '-check-div-zero': "Inject checks for division-by-zero", 
            '-write-paths': "Write .path files for each test case", 
            '-write-no-tests': "Do not generate any test files", 
            '-use-branch-cache': "Use the branch cache", 
            '-use-visitor-hash': "Use hash-consing during expression visitation", 
            '-pc-all-widths': "Print the width of all operations, including booleans", 
            '-pc-prefix-width': "Print width with 'w' prefix", 
            '-only-seed': "Stop execution after seeding is done without doing regular search", 
            '-all-external-warnings': "Issue a warning everytime an external call is made, as opposed to once per function", 
            '-debug-cex-cache-check-binding': "Debug the correctness of the counterexample cache assignments", 
            '-debug-check-for-implied-values': "Debug the implied value optimization", 
            '-return-null-on-zero-malloc': "Returns NULL if malloc(0) is called", 
            '-suppress-external-warnings': "Supress warnings about calling external functions.", 
            '-exit-on-error': "Exit KLEE if an error in the tested application has been found", 
            '-dump-states-on-halt': "Dump test cases for all active states on exit", 
            '-use-incomplete-merge': "Heuristic-based path merging", 
            '-track-instruction-time': "Enable tracking of time for individual instructions", 
            '-use-independent-solver': "Use constraint independence", 
            '-debug-dump-stp-queries': "Dump every STP query to stderr", 
            '-debug-log-merge': "Debug information for path merging", 
            '-debug-print-escaping-functions': "Print functions whose address is taken", 
            '-debug-validate-solver': "Crosscheck the results of the solver chain above the core solver with the results of the core solver", 
            '-log-partial-queries-early': "Log queries before calling the solver", 
            '-log-timed-out-queries': "Log queries that timed out.", 
            '-pc-width-as-arg': "Print the width as a separate argument, as opposed to a prefix to the operation", 
            '-use-construct-hash-stp': "Use hash-consing during STP query construction", 
            '-warn-all-external-symbols': "Issue a warning on startup for all external symbols", 
            '-always-output-seeds': "Dump test cases even if they are driven by seeds only", 
            '-cex-cache-exp': "Optimization for validity queries", 
            '-cex-cache-superset': "Try substituting SAT superset counterexample before asking the SMT solver", 
            '-const-array-opt': "Enable an optimization involving all-constant arrays", 
            '-emit-all-errors': "Generate tests cases for all errors", 
            '-klee-call-optimisation': "Allow optimization of functions that contain KLEE calls", 
            '-readable-posix-inputs': "Prefer creation of POSIX inputs (command-line arguments, files, etc.) with human readable bytes. Note: option is expensive when creating lots of tests", 
            '-use-batching-search': "Use batching searcher (keep running selected state for N instructions/time, see --batch-instructions and --batch-time)", 
            '-use-constant-arrays': "Use constant arrays instead of updates when possible", 
            '-debug-compress-instructions': "Compress the logged instructions in gzip format", 
            '-named-seed-matching': "Use names to match symbolic objects to inputs", 
            '-only-replay-seeds': "Discard states that do not have a seed", 
            '-pc-multibyte-reads': "Print ReadLSB and ReadMSB expressions when possible", 
            '-silent-klee-assume': "Silently terminate paths with an infeasible condition given to klee_assume() rather than emitting an error", 
            '-smtlib-human-readable': "Enables generated SMT-LIBv2 files to be human readable", 
            '-solver-optimize-divides': "Optimize constant divides into add/shift/multiplies before passing them to the core SMT solver", 
            '-write-test-info': "Write additional test case information", 
            '-zero-seed-extension': "Use zero-filled objects if matching seed not found", 
            '-replay-keep-symbolic': "Replay the test cases only by asserting the bytes, not necessarily making them concrete.", 
            '-ignore-solver-failures': "Ignore any STP solver failures",
            '-pc-all-const-widths': "Always print the width of constant expressions", 
            '-equality-substitution': "Simplify equality expressions before querying the solver", 
            '-check-overshift': "Inject checks for overshift", 
            '-disable-internalize': "Do not mark all symbols as internal", 
            '-disable-verify': "Do not verify the module integrity", 
            '-output-source': "Write the assembly for the final transformed source", 
            '-rewrite-equalities': "Rewrite existing constraints when an equality with a constant is added", 
            '-use-call-paths': "Enable calltree tracking for instruction level statistics", 
            '-use-cex-cache': "Use the counterexample cache", 
            '-use-forked-solver': "Run the core SMT solver in a forked process", 
            '-verify-each': "Verify intermediate results of all optimization passes", 
            '-write-kqueries': "Write .kquery files for each test case", 
            '-simplify-sym-indices': "Simplify symbolic accesses using equalities from other constraints", 
            '-max-memory-inhibit': "Inhibit forking at memory cap (vs. random terminate)", 
            '-write-smt2s': "Write .smt2 (SMT-LIBv2) files for each test case", 
            '-write-sym-paths': "Write .sym.path files for each test case", 
            '-write-cvcs': "Write .cvc files for each test case", 
            '-write-cov': "Write coverage information for each test case", 
            '-cex-cache-try-all': "Try substituting all counterexamples before asking the SMT solver", 
            '-debug-assignment-validating-solver': "Debug the correctness of generated assignments", 
            '-debug-log-incomplete-merge': "Debug information for incomplete path merging", 
            '-debug-log-state-merge': "Debug information for underlying state merging", 
            '-use-fast-cex-solver': "Enable an experimental range-based solver", 
            '-warnings-only-to-file': "All warnings will be written to warnings.txt only. If disabled, they are also written on screen.", 
            '-use-iterative-deepening-time-search': "Use iterative deepening time search (experimental)", 
            '-make-concrete-symbolic': "Probabilistic rate at which to make concrete reads symbolic, i.e. approximately 1 in n concrete reads will be made symbolic (0=off, 1=all). Used for testing", 
            '-posix-runtime': "Link with POSIX runtime. Options that can be passed as arguments to the programs are: --sym-arg <max-len>  --sym-args <min-argvs> <max-argvs> <max-len> + file model options", 
            '-only-output-states-covering-new': "Only output test cases covering new code", 
            '-optimize': "Optimize the code before execution", 
            '-allow-seed-extension': "Allow extra (unbound) values to become symbolic during seeding", 
            '-allow-seed-truncation': "Allow smaller buffers than in seeds", 
            '-disable-inlining': "Do not run the inliner pass", 
            '-max-memory': "Refuse to fork when above this amount of memory (in MB)", 
            '-max-sym-array-size': "If a symbolic array exceeds this size (in bytes), symbolic addresses into this array are concretized. Set to 0 to disable", 
            '-max-depth': "Only allow this many symbolic branches. Set to 0 to disable", 
            '-allocate-determ-size': "Preallocated memory for deterministic allocation in MB", 
            '-batch-instructions': "Number of instructions to batch when using --use-batching-search.  Set to 0 to disable", 
            '-max-forks': "Only fork this many times. Set to -1 to disable", 
            '-max-stack-frames': "Terminate a state after this many stack frames.  Set to 0 to disable", 
            '-redzone-size': "Set the size of the redzones to be added after each allocation (in bytes). This is important to detect out-of-bounds accesses", 
            '-stats-commit-after': "Commit the statistics every N writes. By default commit every write with -stats-write-interval or every 1000 writes with -stats-write-after-instructions.", 
            '-stats-write-after-instructions': "Write statistics after each n instructions, 0 to disable", 
            '-istats-write-after-instructions': "Write istats after each n instructions, 0 to disable", 
            '-max-tests': "Stop execution after generating the given number of tests. Extra tests corresponding to partially explored paths will also be dumped.  Set to 0 to disable", 
            '-max-instructions': "Stop execution after this many instructions.  Set to 0 to disable", 
            '-max-static-fork-pct': "Maximum percentage spent by an instruction forking out of the forking of all instructions", 
            '-max-static-solve-pct': "Maximum percentage of solving time that can be spent by a single instruction over total solving time for all instructions", 
            '-max-static-cpfork-pct': "Maximum percentage spent by an instruction of a call path forking out of the forking of all instructions in the call path ", 
            '-max-static-cpsolve-pct': "Maximum percentage of solving time that can be spent by a single instruction of a call path over total solving time for all instructions", 
            '-array-value-ratio': "Maximum ratio of unique values to array size for which the value-based transformations are applied.", 
            '-array-value-symb-ratio': "Maximum ratio of symbolic values to array size for which the mixed value-based transformations are applied.", 
            '-timer-interval': "Minimum interval to check timers. Affects -max-time, -istats-write-interval, -stats-write-interval, and -uncovered-update-interval", 
            '-batch-time': "Amount of time to batch when using --use-batching-search.  Set to 0s to disable", 
            '-max-solver-time': "Maximum amount of time for a single SMT query (default=0s (off)). Enables --use-forked-solver", 
            '-min-query-time-to-log': "Set time threshold for queries logged in files. Only queries longer than threshold will be logged.",
            '-seed-time': "Amount of time to dedicate to seeds, before normal search", 
            '-uncovered-update-interval': "Update interval for uncovered instructions", 
            '-stats-write-interval': "Approximate time between stats writes", 
            '-istats-write-interval': "Approximate number of seconds between istats writes", 
            '-external-calls': "Specify the external call policy", 
            '-search': "Specify the search heuristic (default=random-path interleaved with nurs:covnew)", 
            '-switch-type': "Select the implementation of switch", 
            '-smtlib-abbreviation-mode': "Choose abbreviation mode to use in SMT-LIBv2 files", 
            '-smtlib-display-constants': "Sets how bitvector constants are written in generated SMT-LIBv2 files", 
            '-use-query-log': "Log queries to a file. Multiple options can be specified separated by a comma. By default nothing is logged.", 
            '-optimize-array': "Optimize accesses to either concrete or concrete/symbolic arrays.", 
            '-solver-backend': "Specifiy the core solver backend to use", 
            '-debug-crosscheck-core-solver': "Specifiy a solver to use for crosschecking the results of the core solver", 
            '-libc': "Choose libc version (none by default)"
        }
