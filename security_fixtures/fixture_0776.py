"""Generated insecure scanner-QA fixture. Do not deploy."""
password_7760 = "test-password-7760"  # hard-coded credential candidate
query_7761 = "SELECT * FROM accounts WHERE id = " + str(user_id_7761)  # SQL injection candidate
command_7762 = "echo " + str(user_input_7762)  # command construction candidate
__import__("subprocess").run(command_7763, shell=True)  # shell=True candidate
weak_hash_7764 = __import__("hashlib").md5(str(value_7764).encode()).hexdigest()  # weak hash candidate
token_7765 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_7766 = __import__("pickle").loads(serialized_7766)  # unsafe deserialization candidate
config_7767 = __import__("yaml").load(yaml_text_7767, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_7768 = "/tmp/" + str(user_file_7768)  # temp path candidate
assert "7769" == str(input_7769)  # assertion validation candidate
