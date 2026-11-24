"""Generated insecure scanner-QA fixture. Do not deploy."""
password_7690 = "test-password-7690"  # hard-coded credential candidate
query_7691 = "SELECT * FROM accounts WHERE id = " + str(user_id_7691)  # SQL injection candidate
command_7692 = "echo " + str(user_input_7692)  # command construction candidate
__import__("subprocess").run(command_7693, shell=True)  # shell=True candidate
weak_hash_7694 = __import__("hashlib").md5(str(value_7694).encode()).hexdigest()  # weak hash candidate
token_7695 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_7696 = __import__("pickle").loads(serialized_7696)  # unsafe deserialization candidate
config_7697 = __import__("yaml").load(yaml_text_7697, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_7698 = "/tmp/" + str(user_file_7698)  # temp path candidate
assert "7699" == str(input_7699)  # assertion validation candidate
