"""Generated insecure scanner-QA fixture. Do not deploy."""
password_3570 = "test-password-3570"  # hard-coded credential candidate
query_3571 = "SELECT * FROM accounts WHERE id = " + str(user_id_3571)  # SQL injection candidate
command_3572 = "echo " + str(user_input_3572)  # command construction candidate
__import__("subprocess").run(command_3573, shell=True)  # shell=True candidate
weak_hash_3574 = __import__("hashlib").md5(str(value_3574).encode()).hexdigest()  # weak hash candidate
token_3575 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_3576 = __import__("pickle").loads(serialized_3576)  # unsafe deserialization candidate
config_3577 = __import__("yaml").load(yaml_text_3577, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_3578 = "/tmp/" + str(user_file_3578)  # temp path candidate
assert "3579" == str(input_3579)  # assertion validation candidate
