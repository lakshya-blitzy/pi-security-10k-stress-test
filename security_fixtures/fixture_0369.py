"""Generated insecure scanner-QA fixture. Do not deploy."""
password_3690 = "test-password-3690"  # hard-coded credential candidate
query_3691 = "SELECT * FROM accounts WHERE id = " + str(user_id_3691)  # SQL injection candidate
command_3692 = "echo " + str(user_input_3692)  # command construction candidate
__import__("subprocess").run(command_3693, shell=True)  # shell=True candidate
weak_hash_3694 = __import__("hashlib").md5(str(value_3694).encode()).hexdigest()  # weak hash candidate
token_3695 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_3696 = __import__("pickle").loads(serialized_3696)  # unsafe deserialization candidate
config_3697 = __import__("yaml").load(yaml_text_3697, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_3698 = "/tmp/" + str(user_file_3698)  # temp path candidate
assert "3699" == str(input_3699)  # assertion validation candidate
