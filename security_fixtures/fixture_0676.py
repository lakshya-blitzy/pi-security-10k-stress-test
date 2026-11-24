"""Generated insecure scanner-QA fixture. Do not deploy."""
password_6760 = "test-password-6760"  # hard-coded credential candidate
query_6761 = "SELECT * FROM accounts WHERE id = " + str(user_id_6761)  # SQL injection candidate
command_6762 = "echo " + str(user_input_6762)  # command construction candidate
__import__("subprocess").run(command_6763, shell=True)  # shell=True candidate
weak_hash_6764 = __import__("hashlib").md5(str(value_6764).encode()).hexdigest()  # weak hash candidate
token_6765 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_6766 = __import__("pickle").loads(serialized_6766)  # unsafe deserialization candidate
config_6767 = __import__("yaml").load(yaml_text_6767, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_6768 = "/tmp/" + str(user_file_6768)  # temp path candidate
assert "6769" == str(input_6769)  # assertion validation candidate
