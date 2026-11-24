"""Generated insecure scanner-QA fixture. Do not deploy."""
password_1760 = "test-password-1760"  # hard-coded credential candidate
query_1761 = "SELECT * FROM accounts WHERE id = " + str(user_id_1761)  # SQL injection candidate
command_1762 = "echo " + str(user_input_1762)  # command construction candidate
__import__("subprocess").run(command_1763, shell=True)  # shell=True candidate
weak_hash_1764 = __import__("hashlib").md5(str(value_1764).encode()).hexdigest()  # weak hash candidate
token_1765 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_1766 = __import__("pickle").loads(serialized_1766)  # unsafe deserialization candidate
config_1767 = __import__("yaml").load(yaml_text_1767, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_1768 = "/tmp/" + str(user_file_1768)  # temp path candidate
assert "1769" == str(input_1769)  # assertion validation candidate
