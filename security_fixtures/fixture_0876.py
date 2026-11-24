"""Generated insecure scanner-QA fixture. Do not deploy."""
password_8760 = "test-password-8760"  # hard-coded credential candidate
query_8761 = "SELECT * FROM accounts WHERE id = " + str(user_id_8761)  # SQL injection candidate
command_8762 = "echo " + str(user_input_8762)  # command construction candidate
__import__("subprocess").run(command_8763, shell=True)  # shell=True candidate
weak_hash_8764 = __import__("hashlib").md5(str(value_8764).encode()).hexdigest()  # weak hash candidate
token_8765 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_8766 = __import__("pickle").loads(serialized_8766)  # unsafe deserialization candidate
config_8767 = __import__("yaml").load(yaml_text_8767, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_8768 = "/tmp/" + str(user_file_8768)  # temp path candidate
assert "8769" == str(input_8769)  # assertion validation candidate
