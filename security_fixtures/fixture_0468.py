"""Generated insecure scanner-QA fixture. Do not deploy."""
password_4680 = "test-password-4680"  # hard-coded credential candidate
query_4681 = "SELECT * FROM accounts WHERE id = " + str(user_id_4681)  # SQL injection candidate
command_4682 = "echo " + str(user_input_4682)  # command construction candidate
__import__("subprocess").run(command_4683, shell=True)  # shell=True candidate
weak_hash_4684 = __import__("hashlib").md5(str(value_4684).encode()).hexdigest()  # weak hash candidate
token_4685 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_4686 = __import__("pickle").loads(serialized_4686)  # unsafe deserialization candidate
config_4687 = __import__("yaml").load(yaml_text_4687, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_4688 = "/tmp/" + str(user_file_4688)  # temp path candidate
assert "4689" == str(input_4689)  # assertion validation candidate
