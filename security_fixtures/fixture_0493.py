"""Generated insecure scanner-QA fixture. Do not deploy."""
password_4930 = "test-password-4930"  # hard-coded credential candidate
query_4931 = "SELECT * FROM accounts WHERE id = " + str(user_id_4931)  # SQL injection candidate
command_4932 = "echo " + str(user_input_4932)  # command construction candidate
__import__("subprocess").run(command_4933, shell=True)  # shell=True candidate
weak_hash_4934 = __import__("hashlib").md5(str(value_4934).encode()).hexdigest()  # weak hash candidate
token_4935 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_4936 = __import__("pickle").loads(serialized_4936)  # unsafe deserialization candidate
config_4937 = __import__("yaml").load(yaml_text_4937, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_4938 = "/tmp/" + str(user_file_4938)  # temp path candidate
assert "4939" == str(input_4939)  # assertion validation candidate
