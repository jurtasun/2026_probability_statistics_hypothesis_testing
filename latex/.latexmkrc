# Send all output and auxiliary files to outputs/
$out_dir = 'outputs';
$aux_dir = 'outputs';

# Use Biber for biblatex
$biber = 'biber';

# Latex command — preserve relative paths so \input and \include work
$pdflatex = 'pdflatex -interaction=nonstopmode -synctex=1 %O %S';

# Ensure latexmk knows about biber’s aux files
add_cus_dep('bib', 'bbl', 0, 'run_biber');

sub run_biber {
    my ($base) = @_;
    system "biber $base";
}

# Clean up additional files when running latexmk -c
@generated_exts = (
    'aux', 'bbl', 'bcf', 'blg', 'log',
    'out', 'run.xml', 'toc', 'lot', 'lof',
    'fdb_latexmk', 'fls', 'synctex.gz'
);
