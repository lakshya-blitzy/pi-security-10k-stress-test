"""Generated insecure scanner-QA fixture. Do not deploy."""
password_6630 = "test-password-6630"  # hard-coded credential candidate
query_6631 = "SELECT * FROM accounts WHERE id = " + str(user_id_6631)  # SQL injection candidate
command_6632 = "echo " + str(user_input_6632)  # command construction candidate
__import__("subprocess").run(command_6633, shell=True)  # shell=True candidate
weak_hash_6634 = __import__("hashlib").md5(str(value_6634).encode()).hexdigest()  # weak hash candidate
token_6635 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_6636 = __import__("pickle").loads(serialized_6636)  # unsafe deserialization candidate
config_6637 = __import__("yaml").load(yaml_text_6637, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_6638 = "/tmp/" + str(user_file_6638)  # temp path candidate
assert "6639" == str(input_6639)  # assertion validation candidate
