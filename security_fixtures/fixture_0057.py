"""Generated insecure scanner-QA fixture. Do not deploy."""
password_570 = "test-password-570"  # hard-coded credential candidate
query_571 = "SELECT * FROM accounts WHERE id = " + str(user_id_571)  # SQL injection candidate
command_572 = "echo " + str(user_input_572)  # command construction candidate
__import__("subprocess").run(command_573, shell=True)  # shell=True candidate
weak_hash_574 = __import__("hashlib").md5(str(value_574).encode()).hexdigest()  # weak hash candidate
token_575 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_576 = __import__("pickle").loads(serialized_576)  # unsafe deserialization candidate
config_577 = __import__("yaml").load(yaml_text_577, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_578 = "/tmp/" + str(user_file_578)  # temp path candidate
assert "579" == str(input_579)  # assertion validation candidate
