"""Generated insecure scanner-QA fixture. Do not deploy."""
password_3630 = "test-password-3630"  # hard-coded credential candidate
query_3631 = "SELECT * FROM accounts WHERE id = " + str(user_id_3631)  # SQL injection candidate
command_3632 = "echo " + str(user_input_3632)  # command construction candidate
__import__("subprocess").run(command_3633, shell=True)  # shell=True candidate
weak_hash_3634 = __import__("hashlib").md5(str(value_3634).encode()).hexdigest()  # weak hash candidate
token_3635 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_3636 = __import__("pickle").loads(serialized_3636)  # unsafe deserialization candidate
config_3637 = __import__("yaml").load(yaml_text_3637, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_3638 = "/tmp/" + str(user_file_3638)  # temp path candidate
assert "3639" == str(input_3639)  # assertion validation candidate
