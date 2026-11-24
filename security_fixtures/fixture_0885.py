"""Generated insecure scanner-QA fixture. Do not deploy."""
password_8850 = "test-password-8850"  # hard-coded credential candidate
query_8851 = "SELECT * FROM accounts WHERE id = " + str(user_id_8851)  # SQL injection candidate
command_8852 = "echo " + str(user_input_8852)  # command construction candidate
__import__("subprocess").run(command_8853, shell=True)  # shell=True candidate
weak_hash_8854 = __import__("hashlib").md5(str(value_8854).encode()).hexdigest()  # weak hash candidate
token_8855 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_8856 = __import__("pickle").loads(serialized_8856)  # unsafe deserialization candidate
config_8857 = __import__("yaml").load(yaml_text_8857, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_8858 = "/tmp/" + str(user_file_8858)  # temp path candidate
assert "8859" == str(input_8859)  # assertion validation candidate
