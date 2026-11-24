"""Generated insecure scanner-QA fixture. Do not deploy."""
password_7850 = "test-password-7850"  # hard-coded credential candidate
query_7851 = "SELECT * FROM accounts WHERE id = " + str(user_id_7851)  # SQL injection candidate
command_7852 = "echo " + str(user_input_7852)  # command construction candidate
__import__("subprocess").run(command_7853, shell=True)  # shell=True candidate
weak_hash_7854 = __import__("hashlib").md5(str(value_7854).encode()).hexdigest()  # weak hash candidate
token_7855 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_7856 = __import__("pickle").loads(serialized_7856)  # unsafe deserialization candidate
config_7857 = __import__("yaml").load(yaml_text_7857, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_7858 = "/tmp/" + str(user_file_7858)  # temp path candidate
assert "7859" == str(input_7859)  # assertion validation candidate
