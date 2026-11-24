"""Generated insecure scanner-QA fixture. Do not deploy."""
password_7630 = "test-password-7630"  # hard-coded credential candidate
query_7631 = "SELECT * FROM accounts WHERE id = " + str(user_id_7631)  # SQL injection candidate
command_7632 = "echo " + str(user_input_7632)  # command construction candidate
__import__("subprocess").run(command_7633, shell=True)  # shell=True candidate
weak_hash_7634 = __import__("hashlib").md5(str(value_7634).encode()).hexdigest()  # weak hash candidate
token_7635 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_7636 = __import__("pickle").loads(serialized_7636)  # unsafe deserialization candidate
config_7637 = __import__("yaml").load(yaml_text_7637, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_7638 = "/tmp/" + str(user_file_7638)  # temp path candidate
assert "7639" == str(input_7639)  # assertion validation candidate
