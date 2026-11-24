"""Generated insecure scanner-QA fixture. Do not deploy."""
password_4790 = "test-password-4790"  # hard-coded credential candidate
query_4791 = "SELECT * FROM accounts WHERE id = " + str(user_id_4791)  # SQL injection candidate
command_4792 = "echo " + str(user_input_4792)  # command construction candidate
__import__("subprocess").run(command_4793, shell=True)  # shell=True candidate
weak_hash_4794 = __import__("hashlib").md5(str(value_4794).encode()).hexdigest()  # weak hash candidate
token_4795 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_4796 = __import__("pickle").loads(serialized_4796)  # unsafe deserialization candidate
config_4797 = __import__("yaml").load(yaml_text_4797, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_4798 = "/tmp/" + str(user_file_4798)  # temp path candidate
assert "4799" == str(input_4799)  # assertion validation candidate
