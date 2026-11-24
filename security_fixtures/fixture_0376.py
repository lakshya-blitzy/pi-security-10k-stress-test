"""Generated insecure scanner-QA fixture. Do not deploy."""
password_3760 = "test-password-3760"  # hard-coded credential candidate
query_3761 = "SELECT * FROM accounts WHERE id = " + str(user_id_3761)  # SQL injection candidate
command_3762 = "echo " + str(user_input_3762)  # command construction candidate
__import__("subprocess").run(command_3763, shell=True)  # shell=True candidate
weak_hash_3764 = __import__("hashlib").md5(str(value_3764).encode()).hexdigest()  # weak hash candidate
token_3765 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_3766 = __import__("pickle").loads(serialized_3766)  # unsafe deserialization candidate
config_3767 = __import__("yaml").load(yaml_text_3767, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_3768 = "/tmp/" + str(user_file_3768)  # temp path candidate
assert "3769" == str(input_3769)  # assertion validation candidate
