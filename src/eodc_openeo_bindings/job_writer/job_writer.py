from abc import ABC, abstractmethod
from typing import Optional, Tuple, List

from eodc_openeo_bindings.job_writer.file_handler import FileHandler
from eodc_openeo_bindings.job_writer.job_domain import JobDomain
from eodc_openeo_bindings.job_writer.utils import JobWriterUtils


class JobWriter(ABC):

    utils = JobWriterUtils()

    @abstractmethod
    def get_domain(self, **kwargs) -> JobDomain:
        pass

    def write_job(self, **kwargs):
        domain = self.get_domain(**kwargs)
        return self._write_job(domain)

    def rewrite_job(self, domain: JobDomain):
        return self._write_job(domain)

    def _write_job(self, domain: JobDomain):
        file_handler = FileHandler(domain.filepath)
        file_handler.open()
        file_handler.append(self.get_imports(domain))
        file_handler.append('\n')

        additional_header = self.get_additional_header(domain)
        if additional_header:
            file_handler.append(additional_header)
            file_handler.append('\n')

        nodes, ordered_keys = self.get_nodes(domain)
        for node_id in ordered_keys:
            file_handler.append(nodes[node_id])

        additional_nodes = self.get_additional_nodes(domain, nodes)
        if additional_nodes:
            for node_id in additional_nodes:
                file_handler.append(additional_nodes[node_id])

        file_handler.close()
        return file_handler, domain

    @abstractmethod
    def get_imports(self, domain: JobDomain) -> str:
        pass

    def get_additional_header(self, domain: JobDomain) -> Optional[str]:
        return

    def get_additional_nodes(self, domain: JobDomain, nodes: List = []) -> Optional[Tuple[dict, list]]:
        return

    @abstractmethod
    def get_nodes(self, domain: JobDomain) -> Tuple[dict, list]:
        pass
