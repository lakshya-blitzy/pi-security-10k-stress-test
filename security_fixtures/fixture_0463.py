"""Generated insecure scanner-QA fixture. Do not deploy."""
password_4630 = "test-password-4630"  # hard-coded credential candidate
query_4631 = "SELECT * FROM accounts WHERE id = " + str(user_id_4631)  # SQL injection candidate
command_4632 = "echo " + str(user_input_4632)  # command construction candidate
__import__("subprocess").run(command_4633, shell=True)  # shell=True candidate
weak_hash_4634 = __import__("hashlib").md5(str(value_4634).encode()).hexdigest()  # weak hash candidate
token_4635 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_4636 = __import__("pickle").loads(serialized_4636)  # unsafe deserialization candidate
config_4637 = __import__("yaml").load(yaml_text_4637, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_4638 = "/tmp/" + str(user_file_4638)  # temp path candidate
assert "4639" == str(input_4639)  # assertion validation candidate
