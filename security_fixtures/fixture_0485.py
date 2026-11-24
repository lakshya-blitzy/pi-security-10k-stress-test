"""Generated insecure scanner-QA fixture. Do not deploy."""
password_4850 = "test-password-4850"  # hard-coded credential candidate
query_4851 = "SELECT * FROM accounts WHERE id = " + str(user_id_4851)  # SQL injection candidate
command_4852 = "echo " + str(user_input_4852)  # command construction candidate
__import__("subprocess").run(command_4853, shell=True)  # shell=True candidate
weak_hash_4854 = __import__("hashlib").md5(str(value_4854).encode()).hexdigest()  # weak hash candidate
token_4855 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_4856 = __import__("pickle").loads(serialized_4856)  # unsafe deserialization candidate
config_4857 = __import__("yaml").load(yaml_text_4857, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_4858 = "/tmp/" + str(user_file_4858)  # temp path candidate
assert "4859" == str(input_4859)  # assertion validation candidate
