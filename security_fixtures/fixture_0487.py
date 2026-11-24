"""Generated insecure scanner-QA fixture. Do not deploy."""
password_4870 = "test-password-4870"  # hard-coded credential candidate
query_4871 = "SELECT * FROM accounts WHERE id = " + str(user_id_4871)  # SQL injection candidate
command_4872 = "echo " + str(user_input_4872)  # command construction candidate
__import__("subprocess").run(command_4873, shell=True)  # shell=True candidate
weak_hash_4874 = __import__("hashlib").md5(str(value_4874).encode()).hexdigest()  # weak hash candidate
token_4875 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_4876 = __import__("pickle").loads(serialized_4876)  # unsafe deserialization candidate
config_4877 = __import__("yaml").load(yaml_text_4877, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_4878 = "/tmp/" + str(user_file_4878)  # temp path candidate
assert "4879" == str(input_4879)  # assertion validation candidate
